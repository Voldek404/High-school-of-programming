SELECT
	exp.expedition_id,
	exp.destination,
	exp.status,
	JSON_OBJECT(
		'survival_rate',(
			SELECT COUNT(CASE WHEN em.survived = 'True' THEN 1 END) / COUNT(em.dwarf_id) * 100
			FROM expedition_members em
			WHERE  em.expedition_id = exp.expedition_id
		),

		'atrifacts_value',(
			SELECT COUNT(ea.value)
			FROM expedition_artifacts ea
			WHERE ea.expedition_id = exp.expedition_id
		),

		'discovered_sites',(
			SELECT COUNT(es.site_id)
            		FROM expedition_sites es
            		WHERE es.expedition_id = exp.expedition_id
		),

		'encounter_success_rate',(
			SELECT COUNT(CASE WHEN ec.outcome = 'Success' THEN 1 END) / 
			COUNT(CASE WHEN ec.outcome = 'Fail' THEN 1 END) * 100
			FROM expedition_creatures ec
			WHERE  ec.expedition_id = exp.expedition_id
		),
		'skill_improvement',(
			SELECT SUM(ds2.experience - ds1.experience) 
			FROM dwarf_skills ds1
			JOIN dwarf_skills ds2 ON ds1.dwarf_id = ds2.dwarf_id AND ds1.skill_id = ds2.skill_id
			WHERE ds1.expedition_id = exp.expedition_id 
		),

		'expedition_duration',(
			SELECT DATEDIFF(return_date, departure_date)
			FROM expedition exp
		),

		'overall_success_score', (
			(
				(SELECT COUNT(CASE WHEN em.survived = 'True' THEN 1 END) / COUNT(em.dwarf_id) * 100 
				FROM expedition_members em 
				WHERE em.expedition_id = exp.expedition_id) / 100
			)
			+ 
			(
				(SELECT COUNT(ea.value)
				FROM expedition_artifacts ea
				WHERE ea.expedition_id = exp.expedition_id) / 10000
			)
			+ 
			(
				(SELECT COUNT(es.site_id)
				FROM expedition_sites es
				WHERE es.expedition_id = exp.expedition_id) / 100
			)
			+ 
			(
				(SELECT COUNT(CASE WHEN ec.outcome = 'Success' THEN 1 END) / 
				COUNT(CASE WHEN ec.outcome = 'Fail' THEN 1 END) * 100
				FROM expedition_creatures ec
				WHERE ec.expedition_id = exp.expedition_id) / 100
			)
			+ 
			(
				(SELECT (ds2.experience - ds1.experience) 
				FROM dwarf_skills ds1
				JOIN dwarf_skills ds2 ON ds1.dwarf_id = ds2.dwarf_id AND ds1.skill_id = ds2.skill_id
				WHERE ds1.expedition_id = exp.expedition_id) / 100
			)
		),

		'member_ids',(
			SELECT JSON_ARRAYAGG(em.dwarf_id)
			FROM expedition_members em
			WHERE em.expedition_id = exp.expedition_id
		),

		'artifacts_ids',(
			SELECT JSON_ARRAYAGG(ea.artifacts_id)
			FROM expedition_artifacts ea
			WHERE ea.expedition_id = exp.expedition_id
		),

		'site_ids',(
			SELECT JSON_ARRAYAGG(es.site_id)
			FROM expedition_sites es
			WHERE es.expedition_id = exp.expedition_id
		)
	) AS related_entities
FROM expeditions exp
ORDER BY JSON_EXTRACT(related_entities, '$.overall_success_score') DESC;
