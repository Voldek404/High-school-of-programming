SELECT 
    ms.squad_id,
    ms.name AS squad_name,
    ms.formation_type,
    ms.leader_id AS leader_name,
    COUNT(sb.date) AS total_battles,
    SUM(CASE WHEN sb.outcome = TRUE THEN 1 ELSE 0 END) AS victories,
    ROUND(
        (SUM(CASE WHEN sb.outcome = TRUE THEN 1 ELSE 0 END) * 100.0) / NULLIF(COUNT(sb.date), 0), 
        2
    	) AS victory_percentage,
    SUM(sb.casualties) * 100.0 / NULLIF(COUNT(sm.dwarves_id), 0) AS casualty_rate,
    SUM(sb.casualties) * 1.0 / NULLIF(SUM(ca.casualties), 1) AS casualty_exchange_ratio,
    COUNT(sm.dwarves_id) - SUM(sb.casualties) AS current_members,
    COUNT(sm.dwarves_id) AS total_members_ever,
    ROUND(
        (COUNT(sm.dwarves_id) - SUM(sb.casualties)) * 100.0 / NULLIF(COUNT(sm.dwarves_id), 1), 
        2
    	) AS retention_rate,
    ROUND(SUM(e.quality::DECIMAL) / NULLIF(COUNT(e.quality), 1), 2) AS avg_equipment_quality,
    COUNT(st.squad_id) AS total_training_sessions,
    ROUND(AVG(st.effectiveness), 2) AS avg_training_effectiveness, --- добить
    ROUND(CORR(st.frequency, sb.outcome), 2) AS training_battle_correlation,
    ROUND(AVG(sm.skill_improvement), 2) AS avg_combat_skill_improvement,
    ROUND(
        (SUM(CASE WHEN sb.outcome = TRUE THEN 1 ELSE 0 END) * 0.5 + 
         AVG(st.effectiveness) * 0.3 + 
         AVG(sm.skill_improvement) * 0.2), 
        3
    	) AS overall_effectiveness_score,
    JSON_OBJECT(
        'member_ids', (
		SELECT JSON_ARRAYAGG(m.member_id) FROM squad_members m WHERE m.squad_id = ms.squad_id
	),
        'equipment_ids', (
		SELECT JSON_ARRAYAGG(e.equipment_id) FROM squad_equipment e WHERE e.squad_id = ms.squad_id
	),
        'battle_report_ids', (
		SELECT JSON_ARRAYAGG(b.battle_report_id) FROM battle_reports b WHERE b.squad_id = ms.squad_id
	),
        'training_ids', (
		SELECT JSON_ARRAYAGG(t.training_id) FROM training_sessions t WHERE t.squad_id = ms.squad_id
	)
    ) AS related_entities
FROM military_squad ms
LEFT JOIN squad_battles sb ON sb.squad_id = ms.squad_id
LEFT JOIN squad_members sm ON sm.squad_id = ms.squad_id
LEFT JOIN squad_training st ON st.squad_id = ms.squad_id
LEFT JOIN squad_equipment e ON e.squad_id = ms.squad_id
GROUP BY ms.squad_id;
