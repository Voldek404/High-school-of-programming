SELECT 
    -- Основные статистики
    SUM(sb.attack_id) AS total_recorded_attacks,
    COUNT(DISTINCT sb.creature_id) AS unique_attackers,
    (
        COUNT(CASE WHEN sb.outcome = 'Victory' THEN 1 END) * 100.0 / COUNT(sb.report_id)
    ) AS overall_defense_success_rate,

    -- Оценка угроз
    CASE 
        WHEN SUM(CASE WHEN sb.date >= CURDATE() - INTERVAL 10 DAY THEN 1 END) BETWEEN 0 AND 10 THEN 'Low'
        WHEN SUM(CASE WHEN sb.date >= CURDATE() - INTERVAL 10 DAY THEN 1 END) BETWEEN 10 AND 20 THEN 'Moderate'
        ELSE 'High'
    END AS current_threat_level,

    -- Активные угрозы
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'creature_type', c.name,
            'threat_level', c.threat_level,
            'last_sighting_date', MAX(cs.date),
            'territory_proximity', 
            CASE
                WHEN ABS(cs.creature_x - wz.territory_x) <= 10 AND ABS(cs.creature_y - wz.territory_y) <= 10 THEN 'High'
                WHEN ABS(cs.creature_x - wz.territory_x) <= 20 AND ABS(cs.creature_y - wz.territory_y) <= 20 THEN 'Moderate'
                ELSE 'Low'
            END,
            'estimated_numbers', COUNT(cs.creature_id),
            'creature_ids', JSON_ARRAYAGG(cs.creature_id)
        )
    ) AS active_threats,

    -- Уязвимости
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'zone_id', wz.zone_id,
            'zone_name', wz.name,
            'vulnerability_score', 
            (COUNT(CASE WHEN sb.outcome = 'Victory' THEN 1 END) * 100.0 / COUNT(sb.report_id)),
            'historical_breaches', 
            (
                SELECT COUNT(*)
                FROM SQUAD_BATTLES sb
                WHERE sb.fortress_id = wz.fortress_id AND sb.outcome = 'defeat'
            ),
            'fortification_level', 
            CASE
                WHEN SUM(CASE WHEN eq.quality = 'High' THEN 3 WHEN eq.quality = 'Medium' THEN 2 ELSE 1 END) >= 10
                     AND AVG(ds.level) >= 2
                     AND COUNT(m.squad_id) >= 5 THEN 3
                WHEN SUM(CASE WHEN eq.quality = 'High' THEN 3 WHEN eq.quality = 'Medium' THEN 2 ELSE 1 END) >= 5
                     AND AVG(ds.level) >= 1.5
                     AND COUNT(m.squad_id) >= 3 THEN 2
                ELSE 1
            END
        )
    ) AS vulnerability_analysis,

    -- Время отклика военной силы
    AVG(TIMESTAMPDIFF(SECOND, o.creation_date, o.completion_date)) AS military_response_time,

    -- Покрытие обороны
    JSON_OBJECT(
        'structure_ids', JSON_ARRAYAGG(DISTINCT wz.fortress_id),
        'squad_ids', JSON_ARRAYAGG(DISTINCT m.squad_id)
    ) AS defense_coverage

FROM 
    FORTRESSES f
LEFT JOIN 
    MILITARY_SQUADS ms ON f.fortress_id = ms.fortress_id
LEFT JOIN 
    SQUAD_BATTLES sb ON ms.squad_id = sb.squad_id
LEFT JOIN 
    CREATURES c ON sb.creature_id = c.creature_id
LEFT JOIN 
    CREATURE_SIGHTINGS cs ON c.creature_id = cs.creature_id
LEFT JOIN 
    WORKSHOP_ZONES wz ON wz.fortress_id = f.fortress_id
LEFT JOIN 
    DWARVES d ON f.fortress_id = d.fortress_id
LEFT JOIN 
    DWARF_SKILLS ds ON d.dwarf_id = ds.dwarf_id
LEFT JOIN 
    MILITARY_SQUADS m ON ms.squad_id = m.squad_id
LEFT JOIN 
    SQUAD_EQUIPMENT se ON m.squad_id = se.squad_id
LEFT JOIN 
    EQUIPMENT eq ON se.equipment_id = eq.equipment_id
LEFT JOIN 
    ORDERS o ON o.fortress_id = f.fortress_id

GROUP BY 
    f.fortress_id;

SELECT 
    ms.fortress_id,
    ms.formation_type AS defense_type,
    (COUNT(so.operation_id) FILTER (WHERE so.status = 'Success') * 100.0 / COUNT(so.operation_id)) AS effectiveness_rate,
    COALESCE(AVG(ca.casualties), 0) AS avg_enemy_casualties,
    JSON_ARRAYAGG(ms.fortress_id) AS structure_ids
FROM 
    military_squads ms
LEFT JOIN 
    squad_operations so ON ms.squad_id = so.squad_id
LEFT JOIN 
    squad_battles sb ON ms.squad_id = sb.squad_id
LEFT JOIN 
    creature_attacks ca ON sb.battle_id = ca.battle_id
GROUP BY 
    ms.fortress_id, ms.formation_type
ORDER BY 
    ms.fortress_id;


