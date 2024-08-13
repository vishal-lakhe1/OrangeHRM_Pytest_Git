pytest -v -s -n=4 --html=HTMLReports/myreport_chrome.html --alluredir="AllureReportsChrome" --disable-warnings --browser chrome -m "sanity and group1"

pytest -v -s -n=4 --html=HTMLReports/myreport_edge.html --alluredir="AllureReportsEdge" --disable-warnings --browser edge -m "sanity and group1"

pytest -v -s -n=4 --html=HTMLReports/myreport_firefox.html --alluredir="AllureReportsFirefox" --disable-warnings --browser firefox -m "sanity and group1"