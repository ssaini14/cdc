from bs4 import BeautifulSoup
from datetime import datetime

diff = '''
<table class="diff" id="difflib_chg_to49__top"
       cellspacing="0" cellpadding="0" rules="groups">
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <thead>
    <tr>
        <th class="diff_next"><br/></th>
        <th colspan="2" class="diff_header"><h2><a
                href="http://www.cobbanddouglaspublichealth.com/services/epidemiology-infectious-disease/novelcoronavirus/">Coronavirus
            Disease 2019 (COVID-19) - Cobb & Douglas Public Health</a></h2></th>
        <th class="diff_next"><br/></th>
        <th colspan="2" class="diff_header"></th>
    </tr>
    <tr>
        <th></th>
        <th colspan="2">Previous Article</th>
        <th></th>
        <th colspan="2">Current Article</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_463">463</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_463">463</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_464">464</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_464">464</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_465">465</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_465">465</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next" id="difflib_chg_to49__0"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;you&nbsp;are&nbsp;sick,&nbsp;stay&nbsp;home&nbsp;t</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If&nbsp;you&nbsp;are&nbsp;sick,&nbsp;stay&nbsp;home&nbsp;t</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">o&nbsp;reduce&nbsp;the&nbsp;spread&nbsp;of&nbsp;#COVID19&nbsp;unless&nbsp;you&nbsp;need&nbsp;medical&nbsp;care.&nbsp;Protect&nbsp;yourself&nbsp;a</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">o&nbsp;reduce&nbsp;the&nbsp;spread&nbsp;of&nbsp;#COVID19&nbsp;unless&nbsp;you&nbsp;need&nbsp;medical&nbsp;care.&nbsp;Protect&nbsp;yourself&nbsp;a</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">nd&nbsp;othe&nbsp;twitter.com/i/web/status/1&nbsp;</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">nd&nbsp;othe&nbsp;twitter.com/i/web/status/1&nbsp;</td>
    </tr>
    <tr>
        <td class="diff_next"><a href="#difflib_chg_to49__1">n</a></td>
        <td class="diff_header" id="from49_466">466</td>
        <td nowrap="nowrap"><span class="diff_chg">7</span>&nbsp;hours&nbsp;ago</td>
        <td class="diff_next"><a href="#difflib_chg_to49__1">n</a></td>
        <td class="diff_header" id="to49_466">466</td>
        <td nowrap="nowrap"><span class="diff_chg">10</span>&nbsp;hours&nbsp;ago</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_467">467</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_467">467</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_468">468</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_468">468</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_469">469</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_469">469</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_470">470</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_470">470</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next" id="difflib_chg_to49__1"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is&nbsp;your&nbsp;grocery&nbsp;store&nbsp;out&nbsp;of</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is&nbsp;your&nbsp;grocery&nbsp;store&nbsp;out&nbsp;of</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;your&nbsp;WIC&nbsp;infant&nbsp;formula?&nbsp;Please&nbsp;contact&nbsp;your&nbsp;local&nbsp;WIC&nbsp;clinic&nbsp;and&nbsp;ask&nbsp;for&nbsp;help.</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;your&nbsp;WIC&nbsp;infant&nbsp;formula?&nbsp;Please&nbsp;contact&nbsp;your&nbsp;local&nbsp;WIC&nbsp;clinic&nbsp;and&nbsp;ask&nbsp;for&nbsp;help.</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;Please&nbsp;twitter.com/i/web/status/1&nbsp;</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;Please&nbsp;twitter.com/i/web/status/1&nbsp;</td>
    </tr>
    <tr>
        <td class="diff_next"><a href="#difflib_chg_to49__2">n</a></td>
        <td class="diff_header" id="from49_471">471</td>
        <td nowrap="nowrap">1<span class="diff_chg">0</span>&nbsp;hours&nbsp;ago</td>
        <td class="diff_next"><a href="#difflib_chg_to49__2">n</a></td>
        <td class="diff_header" id="to49_471">471</td>
        <td nowrap="nowrap">1<span class="diff_chg">3</span>&nbsp;hours&nbsp;ago</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_472">472</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_472">472</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_473">473</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_473">473</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_474">474</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_474">474</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_475">475</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_475">475</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next" id="difflib_chg_to49__2"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To&nbsp;ensure&nbsp;the&nbsp;health&nbsp;and&nbsp;saf</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To&nbsp;ensure&nbsp;the&nbsp;health&nbsp;and&nbsp;saf</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">ety&nbsp;of&nbsp;our&nbsp;community,&nbsp;we&nbsp;have&nbsp;limited&nbsp;some&nbsp;of&nbsp;our&nbsp;services&nbsp;at&nbsp;all&nbsp;CDPH&nbsp;locations</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">ety&nbsp;of&nbsp;our&nbsp;community,&nbsp;we&nbsp;have&nbsp;limited&nbsp;some&nbsp;of&nbsp;our&nbsp;services&nbsp;at&nbsp;all&nbsp;CDPH&nbsp;locations</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">.&nbsp;twitter.com/i/web/status/1&nbsp;</td>
        <td class="diff_next"></td>
        <td class="diff_header">></td>
        <td nowrap="nowrap">.&nbsp;twitter.com/i/web/status/1&nbsp;</td>
    </tr>
    <tr>
        <td class="diff_next"><a href="#difflib_chg_to49__top">t</a></td>
        <td class="diff_header" id="from49_476">476</td>
        <td nowrap="nowrap">1<span class="diff_chg">1</span>&nbsp;hours&nbsp;ago</td>
        <td class="diff_next"><a href="#difflib_chg_to49__top">t</a></td>
        <td class="diff_header" id="to49_476">476</td>
        <td nowrap="nowrap">1<span class="diff_chg">4</span>&nbsp;hours&nbsp;ago</td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_477">477</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_477">477</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_478">478</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_478">478</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from49_479">479</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to49_479">479</td>
        <td nowrap="nowrap"></td>
    </tr>
    </tbody>
</table>
'''

diff1 = '''
<table class="diff" id="difflib_chg_to281__top"
       cellspacing="0" cellpadding="0" rules="groups">
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <colgroup></colgroup>
    <thead>
    <tr>
        <th class="diff_next"><br/></th>
        <th colspan="2" class="diff_header"><h2><a href="https://city.milwaukee.gov/Coronavirus#.XnCMeaq6aMo">Novel
            Coronavirus</a></h2></th>
        <th class="diff_next"><br/></th>
        <th colspan="2" class="diff_header"></th>
    </tr>
    <tr>
        <th></th>
        <th colspan="2">Previous Article</th>
        <th></th>
        <th colspan="2">Current Article</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td class="diff_next" id="difflib_chg_to281__0"><a href="#difflib_chg_to281__top">t</a></td>
        <td class="diff_header" id="from281_1">1</td>
        <td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td>
        <td class="diff_next"><a href="#difflib_chg_to281__top">t</a></td>
        <td class="diff_header"></td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from281_2">2</td>
        <td nowrap="nowrap"><span class="diff_sub">&nbsp;</span></td>
        <td class="diff_next"></td>
        <td class="diff_header"></td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from281_3">3</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to281_1">1</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from281_4">4</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to281_2">2</td>
        <td nowrap="nowrap"></td>
    </tr>
    <tr>
        <td class="diff_next"></td>
        <td class="diff_header" id="from281_5">5</td>
        <td nowrap="nowrap"></td>
        <td class="diff_next"></td>
        <td class="diff_header" id="to281_3">3</td>
        <td nowrap="nowrap"></td>
    </tr>
    </tbody>
</table>
'''

# file_path = 'data/response.json'


def remove_empty(json_array):
    for json_object in json_array:
        count = 0
        previous_changes = json_object["previousChanges"]
        for change in previous_changes:
            if len(change["Content"]) == 0:
                count = count + 1
        current_changes = json_object["currentChanges"]
        for change in current_changes:
            if len(change["Content"]) == 0:
                count = count + 1
        if count == 6:
            json_array.remove(json_object)
    return json_array


def get_diff_json_util(rows, url):
    previous_context = ''
    current_context = ''
    previous_context_flag = True
    previous_changes = [{"type": "ADD", "Content": "", "Offset": ""}, {"type": "CHANGE", "Content": "", "Offset": ""},
                        {"type": "DELETE", "Content": "", "Offset": ""}]
    current_changes = [{"type": "ADD", "Content": "", "Offset": ""}, {"type": "CHANGE", "Content": "", "Offset": ""},
                       {"type": "DELETE", "Content": "", "Offset": ""}]
    previous_changes_flag = True
    for tr in rows:
        # for tr in soup.find_all('tr'):
        # log(type(tr))
        # tr = BeautifulSoup(tr, "html.parser")
        for td in tr.find_all('td', nowrap='nowrap'):
            # log(td)
            if td.find('span'):
                if previous_changes_flag:
                    if td.find('span')['class'][0] == 'diff_chg':
                        previous_changes[1]["Content"] = td.find('span').text.strip()
                        previous_changes[1]["Offset"] = len(previous_context) + td.text.strip().find(td.find('span').text.strip())
                    elif td.find('span')['class'][0] == 'diff_add':
                        previous_changes[0]["Content"] = td.find('span').text.strip()
                        previous_changes[0]["Offset"] = len(previous_context) + td.text.strip().find(td.find('span').text.strip())
                    elif td.find('span')['class'][0] == 'diff_sub':
                        previous_changes[2]["Content"] = td.find('span').text.strip()
                        previous_changes[2]["Offset"] = len(previous_context) + td.text.strip().find(td.find('span').text.strip())
                else:
                    if td.find('span')['class'][0] == 'diff_chg':
                        current_changes[1]["Content"] = td.find('span').text.strip()
                        current_changes[1]["Offset"] = len(current_context) + td.text.strip().find(td.find('span').text.strip())
                    elif td.find('span')['class'][0] == 'diff_add':
                        current_changes[0]["Content"] = td.find('span').text.strip()
                        current_changes[0]["Offset"] = len(current_context) + td.text.strip().find(td.find('span').text.strip())
                    elif td.find('span')['class'][0] == 'diff_sub':
                        current_changes[2]["Content"] = td.find('span').text.strip()
                        current_changes[2]["Offset"] = len(current_context) + td.text.strip().find(td.find('span').text.strip())
                previous_changes_flag = not previous_changes_flag
            if previous_context_flag:
                previous_context = previous_context + td.text.strip()
            else:
                current_context = current_context + td.text.strip()
            previous_context_flag = not previous_context_flag
    response = {"url": url,
                "createdatetime": datetime.now(),
                "previousContext": previous_context.replace('\xa0', ' '),
                "currentContext": current_context.replace('\xa0', ' '),
                "previousChanges": previous_changes,
                "currentChanges": current_changes}
    return response


def get_diff_json(diff, url):
    soup = BeautifulSoup(diff, "html.parser")
    soup = soup.find('tbody')
    table_row_change = []
    res = []

    for tr in soup.find_all('tr'):
        table_row_change.append(tr)
        if tr.find('td').find('a'):
            res.append(get_diff_json_util(table_row_change, url))
            table_row_change.clear()

    # log(json.dumps(res))

    res = remove_empty(res)
    # if len(res) > 0:
    #     with open(file_path, "a") as outfile:
    #         outfile.write(json.dumps(res))
    return res


get_diff_json(diff, 'njfnsa')