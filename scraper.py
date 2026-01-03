import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_website_contents(url):
    """
    GitHub sayfaları için özel optimize edilmiş içerik çekici.
    Bütün sayfayı değil, sadece repository listesini hedefler.
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return f"Hata: Sayfa yüklenemedi (Kod: {response.status_code})"

        soup = BeautifulSoup(response.content, "html.parser")
        
        extracted_text = []
        
        repo_list = soup.find(id="user-repositories-list")
        
        if repo_list:
            repos = repo_list.find_all('li')
            for repo in repos:
                name_tag = repo.find('h3')
                desc_tag = repo.find('p', itemprop='description')
                lang_tag = repo.find('span', itemprop='programmingLanguage')
                
                repo_info = ""
                if name_tag:
                    repo_info += f"REPO ADI: {name_tag.get_text(strip=True)}\n"
                if desc_tag:
                    repo_info += f"AÇIKLAMA: {desc_tag.get_text(strip=True)}\n"
                if lang_tag:
                    repo_info += f"DİL: {lang_tag.get_text(strip=True)}\n"
                
                repo_info += "-" * 20 # Ayıraç
                extracted_text.append(repo_info)
                
        else:
            for h3 in soup.find_all('h3'):
                link = h3.find('a')
                if link:
                    text = link.get_text(strip=True)
                    href = link.get('href', '')
                    extracted_text.append(f"Olası Repo: {text} (Link: https://github.com{href})")

        if not extracted_text:
            return "Özel ayıklama başarısız, ham metin dönülüyor:\n" + soup.body.get_text(separator='\n', strip=True)[:10000]

        return "\n".join(extracted_text)

    except Exception as e:
        return f"Scraper hatası: {str(e)}"