run:
	scrapy crawl supplier_collection

start:
	scrapy crawl supplier_collection -s JOBDIR=crawls/supplier_collection
