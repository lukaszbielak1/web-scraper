from ..web_scraper.web_scraper import Mazda_Cars

class Test_Mazda_Cars:
    def test_get_all_cars_non_empty(self):
        assert len(Mazda_Cars().get_all_cars()) > 0