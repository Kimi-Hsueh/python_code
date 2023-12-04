select 站點名稱,MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借數量,可還車
FROM 台北市youbike
GROUP BY 站點名稱


