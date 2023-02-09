-- SQL scrip that list all bands with Glam rock as their main styleranked by their longevity
SELECT band_name, 
CASE
	WHEN split is NULL THEN (2020 - formed)
	ELSE (split - formed)
END
AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
