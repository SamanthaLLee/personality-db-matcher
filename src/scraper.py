

from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import constants

options = Options()
options.headless = True
url = constants.url


def get_profile_slugs():
    # driver = webdriver.Chrome(
    #     options=options, executable_path=constants.DRIVER_PATH)
    # driver = webdriver.PhantomJS()
    # driver.get(url+"/profile?personality=9")
    # html = driver.page_source

    # time.sleep(2)
    # html = driver.execute_script('return document.documentElement.outerHTML')
    # driver.quit()

    session = HTMLSession()
    resp = session.get(url+"/profile?personality=9")
    resp.html.render(sleep=2)
    html = resp.html.html

    soup = BeautifulSoup(html, 'lxml')
    slugs = []
    limit = 2
    counter = 0
    for a in soup.find_all("a", {"class": "profile-card-link"}):
        slugs.append(a['href'])
        counter += 1
        if counter > limit:
            break
    print(slugs)


def get_profile_details():
    # driver = webdriver.Chrome(
    #     options=options, executable_path=constants.DRIVER_PATH)
    # driver.get(url+"/profile/808/")
    # time.sleep(2)
    # html = driver.execute_script('return document.documentElement.outerHTML')
    # driver.quit()

    session = HTMLSession()
    resp = session.get(url+"/profile/808/")
    resp.html.render(sleep=2)
    html = resp.html.html

    soup = BeautifulSoup(html, 'lxml')
    profile = soup.find("div", {"class": "profile-personality"})
    stripped_profile = ''.join(str(x) for x in profile.contents)

    personalities = stripped_profile.split(" - ")

    print(personalities)


def score_profile():
    profile = ['INFJ', '6w5', 'sp/so', '612', 'EII',
               'RLOAI', 'LEVF', 'Phlegmatic-Melancholic']
    user = ['INFJ', '3w2', 'so/sx', '315', 'EII',
            'RLOAI', 'VELF', 'Phlegmatic-Melancholic']

    score = 0

    for i, u_type in enumerate(user):
        p_type = profile[i]
        # MBTI
        if i == 0:
            # Same personality
            if u_type == p_type:
                score += 4
            # Different personality, check for similarities
            else:
                for letter in range(4):
                    if u_type[letter] == p_type[letter]:
                        score += 1
        # Enneagram
        elif i == 1:
            # Same dom and wings
            if u_type == p_type:
                score += 4
            # Swapped doms and wings
            elif u_type[0] == p_type[2] and u_type[2] == p_type[0]:
                score += 3
            # Same dom, different wings
            elif u_type[0] == p_type[0]:
                score += 2
            # User's dom is profile's wing
            elif u_type[0] == p_type[2]:
                score += 1
        # Instinctual Variant
        elif i == 2:
            if u_type == p_type:
                score += 5
            else:
                u_variants = u_type.split('/')
                p_variants = p_type.split('/')

                # Same primary
                if u_variants[0] == p_variants[0]:
                    score += 4
                # Switched variants
                elif u_variants[0] == p_variants[1] and u_variants[1] == p_variants[0]:
                    score += 3
                # User's primary is profile's secondary
                elif u_variants[0] == p_variants[1]:
                    score += 2
                # User's secondary is profile's primary
                elif u_variants[1] == p_variants[0]:
                    score += 1
        # Tritype
        elif i == 3:
            # Same tritype
            if u_type == p_type:
                score += 6
            else:
                for num_u in range(3):
                    for num_p in range(3):
                        # Same letter in same location
                        if num_u == num_p and u_type[num_u] == p_type[num_p]:
                            score += 2
                        # Shared letter, different location
                        elif u_type[num_u] == p_type[num_p]:
                            score += 1
        # Socionics
        elif i == 4:
            continue
        # Big 5
        elif i == 5:
            for letter in range(4):
                if u_type[letter] == p_type[letter]:
                    score += 1
        # Attitudinal Psyche
        elif i == 6:
            if u_type == p_type:
                score += 1
            elif p_type in constants.attitudinal_psyche_categories.get(u_type):
                score += 1
        # Temperaments
        elif i == 7:
            # Same temperament
            if u_type == p_type:
                score += 1
            # Same dominant temperament
            elif u_type[0] == p_type[0]:
                score += 1
            else:
                u_temps = u_type.split('-')
                p_temps = p_type.split('-')
                # Swapped temperaments
                if u_temps[0] == p_temps[1] and u_temps[1] == p_temps[0]:
                    score += 1
                # User's dominant temperament is profile's secondary
                elif u_temps[0] == p_temps[1]:
                    score += 1
                # User's secondary temperament is profile's dominant
                elif u_temps[1] == p_temps[0]:
                    score += 1

    print(score)


get_profile_slugs()
score_profile()
