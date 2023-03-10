### Challenge
# 1. 또 다른 구직 웹사이트에 대한 job extractor 만들기
# 2. 더 많은 page에서 data 수집하기
from extractors.wwr import wwr_extractor
from extractors.indeed import indeed_extractor
from fileCreator import save_to_file
from flask import Flask, render_template, request, redirect, send_file

db={}

app = Flask("JobScrapper")
#syntatic sugar
@app.route("/") #decorator: 해당 경로로 접속하면 바로 아래의 코드가 실행되도록 약속
def home():
    return render_template("home.html") # Flask는 default로 templates라는 폴더를 탐색한다
@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if (keyword == None) or (keyword == ""):
        return redirect("/")
    if keyword in db:
        jobs=db[keyword]
    else:
        wwr = wwr_extractor(keyword)
        indeed = indeed_extractor(keyword)
        jobs = wwr+indeed
        db[keyword]=jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)
@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if (keyword == None) or (keyword == ""):
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    jobs = db[keyword]
    save_to_file(keyword, jobs)
    return send_file(f"{keyword}.csv", as_attachment=True)
# It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
if __name__=="__main__":
    app.run("127.0.0.1", debug=True)

