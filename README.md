set <password> in imdb.pipelines to store data to mongo

start splash before running splash script using
sudo docker run -it -p 8050:8050 scrapinghub/splash

arguements are given while crawling using -a city="examplecity" and 
can be accessed simply using self.city

curl http://localhost:6800/schedule.json -d project=imdb -d spider=bestmovies
curl http://localhost:6800/cancel.json -d project=imdb -d job=12b6b52691ec11eaaec1fc777410e668
