WITH workshops_stats AS (
    SELECT 
        w.workshop_id,
        w.workshop_name,
        w.workshop_type,
        COUNT(wc.dwarf_id) AS num_craftsdwarves,
        SUM(wp.quantity) AS total_quantity_produced,
        COUNT(wp.product_id) AS total_production_value,
        SUM(wp.quantity::DECIMAL) / COUNT(DISTINCT wp.production_date) AS daily_production_rate,
        SUM(wp.quantity::DECIMAL) / SUM(wm.quantity) AS value_per_material_unit,
        (SUM(wm.quantity::DECIMAL) / SUM(wp.quantity)) AS material_conversion_ratio,
        SUM(ds.skill_id::DECIMAL) / COUNT(d.dwarf_id) AS average_craftsdwarf_skill,
        CORR(SUM(ds.skill_id::DECIMAL) / COUNT(d.dwarf_id), w.quality) AS skill_quality_correlation,
        SUM(wm.quantity::DECIMAL) / SUM(wp.quantity) AS workshop_utilization_percent
    FROM 
        workshops w
    LEFT JOIN 
        workshop_craftsdwarves wc ON w.workshop_id = wc.workshop_id
    LEFT JOIN 
        workshop_products wp ON w.workshop_id = wp.workshop_id
    LEFT JOIN 
        workshop_materials wm ON w.workshop_id = wm.workshop_id
    LEFT JOIN 
        dwarves d ON d.fortress_id = w.fortress_id
    LEFT JOIN 
        dwarf_skills ds ON ds.dwarf_id = d.dwarf_id
    GROUP BY 
        w.workshop_id, w.workshop_name, w.workshop_type, w.quality
),
related_entities AS (
    SELECT 
        w.workshop_id,
        JSON_OBJECT(
            'craftsdwarf_ids', (
                SELECT JSON_ARRAYAGG(wc.dwarf_id)
                FROM workshop_craftsdwarves wc
                WHERE wc.workshop_id = w.workshop_id
            ),
            'product_ids', (
                SELECT JSON_ARRAYAGG(p.product_id)
                FROM product p
                WHERE p.product_id IN (
                    SELECT wp.product_id
                    FROM workshop_products wp
                    WHERE wp.workshop_id = w.workshop_id
                )
            ),
            'material_ids', (
                SELECT JSON_ARRAYAGG(wm.material_id)
                FROM workshop_materials wm
                WHERE wm.workshop_id = w.workshop_id
            ),
            'project_ids', (
                SELECT JSON_ARRAYAGG(p.project_id)
                FROM projects p
                WHERE p.workshop_id = w.workshop_id
            )
        ) AS related_entities
    FROM workshops w
)
SELECT 
    ws.workshop_id,
    ws.workshop_name,
    ws.workshop_type,
    ws.num_craftsdwarves,
    ws.total_quantity_produced,
    ws.total_production_value,
    ws.daily_production_rate,
    ws.value_per_material_unit,
    ws.material_conversion_ratio,
    ws.average_craftsdwarf_skill,
    ws.skill_quality_correlation,
    ws.workshop_utilization_percent,
    re.related_entities
FROM 
    workshops_stats ws
JOIN 
    related_entities re ON ws.workshop_id = re.workshop_id;
