SELECT COUNT(*) FROM  COUNTRIES WHERE COUNTRIES.MIN_SIZE <= (SELECT MAX(FAMILY_SIZE) FROM FAMILIES ORDER BY DESC LIMIT 1);