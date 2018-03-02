from datetime import datetime

from scrapy import Spider, Request
from scrapy_splash import SplashRequest
from test_spider.items import TestSpiderItem
from w3lib.url import url_query_parameter


from ..db_client import Connector


script = """
function main(splash)
  splash:init_cookies(splash.args.cookies)
  assert(splash:go{
    splash.args.url,
    headers=splash.args.headers,
    http_method=splash.args.http_method,
    body=splash.args.body,
    })
  assert(splash:wait(0.5))

  local entries = splash:history()
  local last_response = entries[#entries].response
  return {
    url = splash:url(),
    headers = last_response.headers,
    http_status = last_response.status,
    cookies = splash:get_cookies(),
    html = splash:html(),
  }
end
"""


class TestTaskSpider(Spider):
    name = "test_spider"
    conn = Connector()

    def start_requests(self):
        base_urls = self.conn.get_urls()

        for url in base_urls:
            # print(url)
            yield SplashRequest(
                url=url,
                # url="https://ru.cryptonator.com/rates/convert/?amount=1&primary=btc&secondary=ltc&source=liverates",
                # callback=self.get_coocie,
                callback=self.parse_curr,
                endpoint="execute",
                cache_args=["lua_source"],
                args={
                    "lua_source": script,
                },
                meta={'dont_redirect': True},
                dont_filter=True
            )
            # break

    def parse_curr(self, resp):
        # print(resp.text)
        curr_val = resp.xpath('/html/body/div/div/div/h2/strong/text()').extract()
        # print(curr_val)
        if curr_val:
            # print(curr_val)
            curr_val = "".join(curr_val)
            curr_val = "".join(curr_val.split())
            try:
                curr_val = float(curr_val)
            except Exception:
                curr_val = None
        else:
            curr_val = None

        # print(curr_val)
        if curr_val:

            from_cur = url_query_parameter(resp.url, "primary")
            to_cur = url_query_parameter(resp.url, "secondary")

            corr_id = self.conn.get_corr_id(from_cur.upper(), to_cur.upper())
            # print(corr_id)
            if corr_id:
                item = TestSpiderItem()
                item["value"] = curr_val
                item["corr_id"] = corr_id
                yield item

        base_urls = self.conn.get_urls()
        for url in base_urls:
            yield SplashRequest(
                url=url,
                # url="https://ru.cryptonator.com/rates/convert/?amount=1&primary=btc&secondary=ltc&source=liverates",
                # callback=self.get_coocie,
                callback=self.parse_curr,
                endpoint="execute",
                cache_args=["lua_source"],
                args={
                    "lua_source": script,
                },
                meta={'dont_redirect': True},
                dont_filter=True
            )


