import streamlit as st
import scraper
import json

# Adding custom HTML meta tags for SEO
st.markdown(
    """
    <meta name="description" content="Convert ChatGPT conversations into a JSON dataset.">
    <meta name="keywords" content="ChatGPT, scraper, JSON dataset, Streamlit app">
    <meta name="author" content="Your Name">
    """,
    unsafe_allow_html=True
)

st.title('ChatGPT Conversation Scraper')

# Adding a description below the title
st.write("""
    This application will export your ChatGPT conversations into a JSON dataset you can use for more advanced purposes. 
    Simply enter the ChatGPT Share URL and click 'Generate Dataset' to get the JSON file.
    \n You must create the share URL from GPT and use that link, it will not work with the normal URL.
""")

# URL input field left blank
url = st.text_input('Enter your share URL:')

if st.button('Generate Dataset'):
    if not url:
        st.error('Please paste share URL to start.')
    elif '/share/' not in url:
        st.error('Incorrect URL. Please use the share link in the ChatGPT conversation Options.')
    else:
        with st.spinner('Generating dataset...'):
            try:
                data = scraper.scrape_chat(url)
                st.success('Dataset generation completed!')
                
                st.json(data)
                
                json_data = json.dumps(data, ensure_ascii=False, indent=4)
                st.download_button(label='Download JSON', data=json_data, file_name='conversation.json', mime='application/json')
            except Exception as e:
                st.error(f'Error: {e}')
