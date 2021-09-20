from pytest import mark
from api_test.get_user import get_users
url="https://gorest.co.in/public/v1/users"


@mark.regression
@mark.sanity
def test_default_page_equal_one():
    json_req1, code1 = get_users(url)
    assert code1 == 200, "Exception. Expected code: 200, actual {code1}"
    json_req2, code2 = get_users(url, {"page":1})
    assert code2 == 200, "Exception. Expected code: 200, actual {code2}"
    assert json_req1 == json_req2, "Results are not equal"



@mark.regression
def test_get_users_all_pages():
    json_req1, code1 = get_users(url)
    assert code1 == 200, "Exception. Expected code: 200, actual {code1}"
    pages_quantity = json_req1['meta']['pagination']['pages']
    #print(pages_quantity)
    for page in range(pages_quantity):
        json_req, code = get_users(url, {"page": (page+1)})
        assert json_req != None, "Should be a valid JSON body"
        assert code == 200, "Exception. Expected code: 200, actual {code}"
        print(code,(page+1))