{{ config(materialized = 'table') }}

SELECT
    symbol,
    COUNT(*) AS symbol_count
FROM (
    SELECT REGEXP_SUBSTR(UNNAMED__0, '\\(([^)]+)\\)', 1, 1, 'e', 1) AS symbol
    FROM DS2508.VKX7SS.WSJGAINERS_20251014_123025
    UNION ALL
    -- (repeat all your WSJ SELECTs here)
    SELECT SYMBOL AS symbol FROM DS2508.VKX7SS.YGAINERS_20251024_160103
)
WHERE symbol IS NOT NULL
GROUP BY symbol
