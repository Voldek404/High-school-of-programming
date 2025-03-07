Task 2.

SELECT 
	d.dwarf_id,
	d.name,
	d.age,
	d.profession,
	JSON_OBJECT(
	   'skill_ids',(
	       SELECT JSON_ARRAYAGG(ds.skill_id)
	       FROM  dwarf_skills ds
	       WHERE d.dwarf_id = ds.dwarf_id
	   ),
	    'assignment_ids',(
	       SELECT JSON_ARRAYAGG(assgnm.assignment_id)
	       FROM dwarf_assignment assgnm 
	       WHERE d.dwarf_id = assgnm.dwarf_id
	   ),
	    'squad_ids',(
               SELECT JSON_ARRAYAGG(ms.squad_id)
	       FROM military_squads ms 
	       WHERE d.fortress_id = ms.fortress_id
	   ),
	   'equipment_ids',(
	       SELECT JSON_ARRAYAGG (de.equipment_id)
	       FROM dwarf_equipment de 
	       WHERE d.dwarf_id = de.dwarf_id
	   )
   ) AS related_entities
FROM dwarves d


Task 3.

SELECT
	ws.workshop_id,
	ws.name,
	ws.type,
	ws.quality,
	JSON_OBJECTS(
		'craftdwarf_ids',(
			SELECT JSON_ARRAYAGG(wc.dwarf_id)
			FROM workshop_craftsdwarves wc 
			WHERE ws.workshop_id = wc.workshop_id
		),
		'project_ids',(
			SELECT JSON_ARRAYAGG(p.project_id)
			FROM projects p 
			WHERE ws.workshop_id = p.workshop_id
		).
		'input_material_ids',(
			SELECT JSON_ARRAYAGG(wm.material_id)
			FROM work_materials wm 
			WHERE ws.workshop_id = wm.workshop_id
		),
		'output_product_ids',(
			SELECT JSON_ARRAYAGG(prod.product_id)
			FROM  products prod
			WHERE wm.material_id = prod.material_id
		)
	) AS related_entities
FROM workshops ws


Task 4.	

SELECT
	ms.squad_id,
	ms.name,
	ms.formation_type,
	ms.leader_id,
	JSON_OBJECTS(
		'member_ids',(
			SELECT JSON_ARRAYAGG(d.dwarf_id)
			FROM dwarves d 
			WHERE ms.fortress_id = d.fortress_id
		),
		'equipment_ids',(
			SELECT JSON_ARRAYAGG(se.equipment_id)
			FROM equipment_id se 
			WHERE ms.squad_id = se.squad_id
		),
		'operation_ids',(
			SELECT JSON_ARRAYAGG(so.operation_id)
			FROM squad_operations so 
			WHERE ms.squad_id = so.squad_id
		),
		'training_schedule_ids',(
			SELECT JSON_ARRAYAGG(st.schedule_id)
			FROM squad_training st 
			WHERE ms.squad_id = st.squad_id
		),
		'battle_reports_ids',(
			SELECT JSON_ARRAYAGG(sb.report_id)
			FROM squad_battles sb 
			WHERE ms.squad_id = sb.squad_id
		)
	) AS related_entities

FROM military_squads ms
