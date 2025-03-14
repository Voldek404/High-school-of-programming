WITH squad_battle_stats AS (
    SELECT 
        sb.squad_id,
        COUNT(sb.date) AS total_battles,
        SUM(CASE WHEN sb.outcome = TRUE THEN 1 ELSE 0 END) AS victories,
        SUM(sb.casualties) AS total_casualties,
        SUM(sb.enemy_casualties) AS total_enemy_casualties
    FROM squad_battles sb
    GROUP BY sb.squad_id
),
squad_member_history AS (
    SELECT 
        sm.squad_id,
        COUNT(DISTINCT sm.dwarves_id) AS total_members_ever,
        COUNT(DISTINCT sm.dwarves_id) - SUM(sb.casualties) AS current_members
    FROM squad_members sm
    LEFT JOIN squad_battles sb ON sm.squad_id = sb.squad_id
    GROUP BY sm.squad_id
),
squad_equipment_quality AS (
    SELECT 
        se.squad_id,
        ROUND(AVG(e.quality::DECIMAL), 2) AS avg_equipment_quality
    FROM squad_equipment se
    JOIN equipment e ON se.equipment_id = e.equipment_id
    GROUP BY se.squad_id
),
squad_training_effectiveness AS (
    SELECT 
        st.squad_id,
        COUNT(st.squad_id) AS total_training_sessions,
        ROUND(AVG(st.effectiveness), 2) AS avg_training_effectiveness, 
        ROUND(CORR(st.frequency, sb.outcome), 2) AS training_battle_correlation
    FROM squad_training st
    LEFT JOIN squad_battles sb ON st.squad_id = sb.squad_id
    GROUP BY st.squad_id
)
SELECT 
    ms.squad_id,
    ms.name AS squad_name,
    ms.formation_type,
    ms.leader_id AS leader_name,
    sbs.total_battles,
    sbs.victories,
    ROUND((sbs.victories * 100.0) / NULLIF(sbs.total_battles, 0), 2) AS victory_percentage,
    ROUND((sbs.total_casualties * 100.0) / NULLIF(smh.total_members_ever, 0), 2) AS casualty_rate,
    ROUND((sbs.total_casualties * 1.0) / NULLIF(sbs.total_enemy_casualties, 1), 2) AS casualty_exchange_ratio,
    smh.current_members,
    smh.total_members_ever,
    ROUND((smh.current_members * 100.0) / NULLIF(smh.total_members_ever, 1), 2) AS retention_rate,
    seq.avg_equipment_quality,
    ste.total_training_sessions,
    ste.avg_training_effectiveness, 
    ste.training_battle_correlation,
    ROUND(AVG(sm.skill_improvement), 2) AS avg_combat_skill_improvement,
    ROUND(
        (sbs.victories * 0.5 + ste.avg_training_effectiveness * 0.3 + AVG(sm.skill_improvement) * 0.2),
        3
    ) AS overall_effectiveness_score,
    JSON_OBJECT(
        'member_ids', (SELECT JSON_ARRAYAGG(m.member_id) FROM squad_members m WHERE m.squad_id = ms.squad_id),
        'equipment_ids', (SELECT JSON_ARRAYAGG(e.equipment_id) FROM squad_equipment e WHERE e.squad_id = ms.squad_id),
        'battle_report_ids', (SELECT JSON_ARRAYAGG(b.battle_report_id) FROM battle_reports b WHERE b.squad_id = ms.squad_id),
        'training_ids', (SELECT JSON_ARRAYAGG(t.training_id) FROM training_sessions t WHERE t.squad_id = ms.squad_id)
    ) AS related_entities
FROM military_squad ms
LEFT JOIN squad_battle_stats sbs ON ms.squad_id = sbs.squad_id
LEFT JOIN squad_member_history smh ON ms.squad_id = smh.squad_id
LEFT JOIN squad_equipment_quality seq ON ms.squad_id = seq.squad_id
LEFT JOIN squad_training_effectiveness ste ON ms.squad_id = ste.squad_id
LEFT JOIN squad_members sm ON ms.squad_id = sm.squad_id
GROUP BY ms.squad_id, ms.name, ms.formation_type, ms.leader_id, sbs.total_battles, sbs.victories, sbs.total_casualties,
    sbs.total_enemy_casualties, smh.current_members, smh.total_members_ever, seq.avg_equipment_quality, ste.total_training_sessions,
    ste.avg_training_effectiveness, ste.training_battle_correlation
ORDER BY overall_effectiveness_score DESC;
