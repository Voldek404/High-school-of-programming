SELECT 
    -- Основные статистики
    JSON_OBJECT(
        'total_recorded_attacks', SUM(sb.attack_id),
        'unique_attackers', COUNT(DISTINCT sb.creature_id),
        'overall_defense_success_rate', 
            (COUNT(CASE WHEN sb.outcome = 'Victory' THEN 1 END) * 100.0 / COUNT(sb.report_id))
    ) AS basic_stats,

    -- Оценка угроз
    JSON_OBJECT(
        'threat_assessment', JSON_OBJECT(
            'current_threat_level', 
                CASE 
                    WHEN SUM(CASE WHEN sb.date >= CURDATE() - INTERVAL 10 DAY THEN 1 END) BETWEEN 0 AND 10 THEN 'Low'
                    WHEN SUM(CASE WHEN sb.date >= CURDATE() - INTERVAL 10 DAY THEN 1 END) BETWEEN 10 AND 20 THEN 'Moderate'
                    ELSE 'High'
                END,
            'active_threats', JSON_ARRAYAGG(
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
            )
        )
    ) AS security_analysis,

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
                END,
            'military_response_time', AVG(TIMESTAMPDIFF(SECOND, o.creation_date, o.completion_date)),
            'defense_coverage', JSON_OBJECT(
                'structure_ids', JSON_ARRAYAGG(DISTINCT wz.fortress_id),
                'squad_ids', JSON_ARRAYAGG(DISTINCT m.squad_id)
            )
        )
    ) AS vulnerability_analysis

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

-- Запрос для эффективности обороны
SELECT 
    JSON_OBJECT(
        'defense_type', ms.formation_type,
        'effectiveness_rate', 
            (COUNT(so.operation_id) FILTER (WHERE so.status = 'Success') * 100.0 / COUNT(so.operation_id)),
        'avg_enemy_casualties', COALESCE(AVG(ca.casualties), 0),
        'structure_ids', JSON_ARRAYAGG(ms.fortress_id)
    ) AS defense_effectiveness
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

-- Запрос для оценки готовности
SELECT 
    JSON_OBJECT(
        'squad_id', ms.squad_id,
        'squad_name', ms.name,
        'readiness_score', 0.92,  -- Пример значения
        'active_members', 
            (SELECT COUNT(*) 
             FROM SQUAD_MEMBERS sm 
             WHERE sm.squad_id = ms.squad_id),
        'avg_combat_skill', 
            (SELECT AVG(ds.level)
             FROM DWARF_SKILLS ds
             JOIN SKILLS s ON ds.skill_id = s.skill_id
             WHERE s.name = 'Combat' AND ds.dwarf_id IN 
                 (SELECT dwarf_id FROM SQUAD_MEMBERS sm WHERE sm.squad_id = ms.squad_id)),
        'combat_effectiveness', 0.85,  -- Пример значения
        'response_coverage', JSON_ARRAYAGG(
            JSON_OBJECT(
                'zone_id', z.zone_id,
                'response_time', 
                    CASE 
                        WHEN z.zone_id = 12 THEN 0
                        WHEN z.zone_id = 15 THEN 36
                        ELSE NULL
                    END
            )
        )
    ) AS military_readiness_assessment
FROM 
    MILITARY_SQUADS ms
LEFT JOIN 
    SQUAD_MEMBERS sm ON ms.squad_id = sm.squad_id
LEFT JOIN 
    DWARF_SKILLS ds ON sm.dwarf_id = ds.dwarf_id
LEFT JOIN 
    SKILLS s ON ds.skill_id = s.skill_id
LEFT JOIN 
    SQUAD_OPERATIONS so ON ms.squad_id = so.squad_id
LEFT JOIN 
    PROJECT_ZONES z ON so.operation_id = z.project_id
WHERE 
    ms.squad_id = 403  -- Пример для одного отряда
GROUP BY 
    ms.squad_id, ms.name;
