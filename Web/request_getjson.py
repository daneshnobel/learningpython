import urllib.request
import json

urlDetail = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02"

def printResults(data):
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    
    count = theJSON["metadata"]["count"]
    print(str(count))

def main():
    webUrl = urllib.request.urlopen(urlDetail)
    statusCode = webUrl.getcode()
    print("The status is "+str(statusCode))
    if statusCode == 200:
        data = webUrl.read()
        printResults(data)


if __name__ == "__main__":
    main()