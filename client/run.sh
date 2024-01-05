# khai báo biến chứa containerId và tên file sẽ chạy
containerId=7133fc9d219a91dc1986fa99aea46d4d75a4fd510c7316c647fb00032647bff9
fileName=group_one_file.py
#chạy docker exec để chạy file
docker exec -it $containerId ./spark/bin/spark-submit /client/$fileName