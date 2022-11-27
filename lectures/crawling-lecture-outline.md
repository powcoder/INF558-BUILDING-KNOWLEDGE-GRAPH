#Definitions
* Basic algorithm
* What it does
* massive vs focused

#Applications
* search
* study of the web
* domain-specific KG
* archiving

#Challenges
* scale
* deduplication
* cost
	* dns
	* fetching
	* parsing/extracting
	* memory/disk
* speed
* errors, redirects
* freshness
* deep web, forms
* counter-crawling/access 
	* login
	* captchas
	* traps
	* fake errors
	* banning
* localization
* dynamic pages
* infinite scrolling
* archiving

#Requirements
* robustness 
* politeness
	* user agent
	* site-wide
	* page-specific
* robots.txt
	* noindex, nocache, nofollow
	* crawl-delay

#Policies, Strategies
* breath first
* depth-first
* quality
* page rank, approximations
* deduplication
	* checksum 
	* shingles
* freshness, revisit
	* new, deleted, changed 
* broad vs deep
* focused crawling
	* URL patterns
	* topic models
* using search engines
* counter-crawling
	* proxies
	* identification of login, captcha, etc
	* user interaction
* hidden/deep web
	* form filling
* dynamic content
	* headless browsers 
* archiving
	* headless browsers, splash
	* digital signatures
	* archive formats, WARC

#Architecture
* basic
	* seed list
	* crawl frontier
	* priority
* multi-threaded
	* single connection to host
* multiple nodes
	* per site
	* per page

#Software
* Scrapy
* Nutch
* ACHE
* scraping hub (service)
* many others

#Evaluation
* quality
	* relevance
	* recall?
* efficiency
	* network
	* CPU 
