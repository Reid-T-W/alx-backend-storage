-- SQL scrip that list all bands with Glam rock as their main styleranked by their longevity
SELECT band_name, (split - formed) as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
