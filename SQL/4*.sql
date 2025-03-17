SELECT JSON_OBJECT(
    'total_trading_partners', COUNT(DISTINCT c.civilization_type),
    'all_time_trade_value', COALESCE(SUM(o.trade_value), 0),
    'all_time_trade_balance', COALESCE(SUM(o.trade_balance), 0),

    'civilization_data', JSON_OBJECT(
        'civilization_trade_data', JSON_ARRAYAGG(
            JSON_OBJECT(
                'civilization_type', c.civilization_type,
                'total_caravans', COUNT(DISTINCT c.caravan_id),
                'total_trade_value', COALESCE(SUM(o.trade_value), 0),
                'trade_balance', COALESCE(SUM(o.trade_balance), 0),
                'trade_relationship', CASE 
                    WHEN SUM(o.trade_balance) > 0 THEN 'Favorable'
                    ELSE 'Unfavorable'
                END,
                'diplomatic_correlation', ROUND(AVG(o.diplomatic_score), 2),
                'caravan_ids', JSON_ARRAYAGG(c.caravan_id)
            )
        )
    ),

    'critical_import_dependencies', JSON_OBJECT(
        'resource_dependency', JSON_ARRAYAGG(
            JSON_OBJECT(
                'material_type', r.material_type,
                'dependency_score', ROUND(SUM(r.dependency_score), 2),
                'total_imported', SUM(r.total_imported),
                'import_diversity', COUNT(DISTINCT r.import_source),
                'resource_ids', JSON_ARRAYAGG(r.resource_id)
            )
        )
    ),

    'export_effectiveness', JSON_OBJECT(
        'export_effectiveness', JSON_ARRAYAGG(
            JSON_OBJECT(
                'workshop_type', w.workshop_type,
                'product_type', w.product_type,
                'export_ratio', ROUND(AVG(w.export_ratio), 2),
                'avg_markup', ROUND(AVG(w.markup), 2),
                'workshop_ids', JSON_ARRAYAGG(w.workshop_id)
            )
        )
    ),

    'trade_timeline', JSON_OBJECT(
        'trade_growth', JSON_ARRAYAGG(
            JSON_OBJECT(
                'year', t.trade_year,
                'quarter', t.trade_quarter,
                'quarterly_value', COALESCE(SUM(t.trade_value), 0),
                'quarterly_balance', COALESCE(SUM(t.trade_balance), 0),
                'trade_diversity', COUNT(DISTINCT t.civilization_type)
            )
        )
    )
) AS trade_report
FROM ORDERS o
JOIN PROJECT_ZONES pz ON o.project_id = pz.project_id
JOIN CARAVANS c ON pz.zone_id = c.fortress_id
LEFT JOIN RESOURCE_IMPORTS r ON o.order_id = r.order_id
LEFT JOIN WORKSHOP_EXPORTS w ON o.order_id = w.order_id
LEFT JOIN TRADE_HISTORY t ON o.order_id = t.order_id
GROUP BY c.civilization_type;
