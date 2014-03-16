#gdalwarp -of GTiff Sidewalk_Inventory.pdf Sidewalk_Inventory3.jpeg

gdal_translate -of GTiff -gcp 460.266 2370.84 -95.3208 38.9283 -gcp 2928.23 2256.23 -95.2049 38.9283 -gcp 3523.03 1702.74 -95.1768 38.9474 -gcp 1096.13 504.646 -95.2866 38.993 -gcp -95.2464 -38.9385 -95.2455 38.938 -gcp -95.2473 -38.9393 -95.2465 38.9387 -gcp -95.2447 -38.9392 -95.244 38.9388 -gcp -95.2445 -38.9369 -95.2436 38.9364 "Sidewalk_Inventory.pdf" "Sidewalk_Inventory_test2.pdf"
gdalwarp -r near -order 1 -co COMPRESS=NONE  "Sidewalk_Inventory_test2.pdf" "Sidewalk_Inventory_modified4.tif"



