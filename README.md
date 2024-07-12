<h1><p align="center">Yandex Taxi Scraper</p></h1>

<p align="center">
  <a href="https://github.com/astrosander/Yandex-Taxi-Scraper" target="blank"><img src="https://github.com/astrosander/Yandex-Taxi-Scraper/assets/69795340/0bed64cc-2711-4086-b78b-91ba7dda1311" width="180" alt="Logo" /></a>
</p>


<h4><p align="center">A scraping tool for searching and locating Yandex Taxi in the specific area</p></h4>
<p align="center">
  <img src="https://github.com/user-attachments/assets/66193b30-3ca9-4992-8680-39695f5d3c2c" width="480" />
</p>

## How it works

The area we are interested in is bounded by a rectangle with opposite vertices with coordinates `PointA` and `PointB`. Since we can only find out about the nearest cars within a radius of about 3 km, we will break our map into segments of this size, and then get information about each segment and remove repetitive information.

<p align="center">
  <img src="https://github.com/astrosander/Yandex-Taxi-Scraper/assets/69795340/7711987a-3bc7-4513-a3bc-c230f6c8b324" width="480" /><br>
  Example of splitting Moscow into equal polygons
</p>
<br><br><br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/0d053aad-6fad-4acb-9c32-d11b4afa8fcd" width="480" /><br>
  Taxi near Domodedovo Airport (Moscow)
</p>
<br><br><br>

<p align="center">
  <img src="https://github.com/astrosander/Yandex-Taxi-Scraper/assets/69795340/b3d93825-cfb6-4fce-98e7-63381495fa60" width="480" />
</p>

<p align="center">
  <img src="https://github.com/astrosander/Yandex-Taxi-Scraper/assets/69795340/96bfbbd2-4e9a-46f0-9a85-f9fbcf4a5d8a" width="480" />
</p>
<p align="center">
  <img src="https://github.com/astrosander/Yandex-Taxi-Scraper/assets/69795340/d1f0be5b-1a34-4da8-99b3-1f28d915b7f2" width="720" />
</p>
