import requests
import streamlit as st
import config
from iex import IEXStock
from datetime import datetime, timedelta

st.set_page_config(page_title="The Stock Watch",
                   page_icon="chart_with_upwards_trend")

st.sidebar.image(
    "https://compote.slate.com/images/926e5009-c10a-48fe-b90e-fa0760f82fcd.png?width=840&rect=680x453&offset=0x30")
st.sidebar.title("The Stock Watch")
st.sidebar.write(
    "Hello, welcome to The Stock Watch. A resource for all kinds of stock information, such as stock overviews, fundamentals, news, and StockTwits updates.")
stock = st.sidebar.text_input("Symbol", value='AMC', max_chars=5)

symbol = IEXStock(config.IEX_API_KEY, stock)

screen = st.sidebar.selectbox(
    'View', ('Overview', 'Fundamentals', 'News', 'Stockwits'))

st.sidebar.subheader("Contact: ")
st.sidebar.write("jacky.chow@stonybrook.edu")
link = '[LinkedIn](https://www.linkedin.com/in/jacchow/)'
st.sidebar.markdown(link, unsafe_allow_html=True)

st.title(screen)
st.header(stock.upper())

if screen == 'Overview':
    logo = symbol.get_logo()

    company_info = symbol.get_company_info()

    col1, col2 = st.beta_columns(2)

    with col1:
        st.image(logo['url'])
    with col2:
        st.write(company_info['companyName'])
        st.write(company_info['exchange'])
        st.subheader('Description')
        st.write(company_info['description'])
        st.subheader('Industry')
        st.write(company_info['industry'])
        st.subheader('Website')
        st.write(company_info['website'])


if screen == 'Fundamentals':
    stats = symbol.get_stats()
    col1, col2 = st.beta_columns(2)

    with col1:
        st.subheader('MarketCap')
        st.write(stats['marketcap'])
        st.subheader('52 week high')
        st.write(stats['week52high'])
        st.subheader('52 week low')
        st.write(stats['week52low'])
        st.subheader("200 day moving average")
        st.write(stats['day200MovingAvg'])
        st.subheader('Shares outstanding')
        st.write(stats['sharesOutstanding'])
        st.subheader('Average 10-day volume')
        st.write(stats['avg10Volume'])
        st.subheader('Dividend Yield')
        st.write(stats['dividendYield'])

    with col2:
        st.subheader('1 year percent change')
        st.write(stats['year1ChangePercent'])
        st.subheader('6 month percent change')
        st.write(stats['month6ChangePercent'])
        st.subheader('1 month percent change')
        st.write(stats['day30ChangePercent'])
        st.subheader('5 day percent change')
        st.write(stats['day5ChangePercent'])
        st.subheader("Trailing 12 months EPS")
        st.write(stats['ttmEPS'])
        st.subheader('Next Earnings Date')
        st.write(stats['nextEarningsDate'])


if screen == 'News':
    news = symbol.get_news()

    for article in news:
        st.subheader(article['headline'])

        dt = datetime.utcfromtimestamp(article['datetime']/1000).isoformat()
        st.write(f"Posted by {article['source']} at {dt}")

        st.write(article['url'])
        st.write(article['summary'])
        st.image(article['image'])
        st.write("")
        st.write("")


if screen == 'Stockwits':
    r = requests.get(
        f'https://api.stocktwits.com/api/2/streams/symbol/{stock}.json')
    data = r.json()

    for message in data['messages']:
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])
