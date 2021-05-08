from flask import Flask, render_template
import Run_Spider
import Read_DB
import Draw_plot


app = Flask(__name__)

@app.route("/")
def crawl_info():
    #step1:runing spider
    Run_Spider.run_spider()
    
    #step2:read info
    Info_dict = Read_DB.read_info()
    Coronavirus_Cases = Info_dict["Coronavirus_Cases"]
    Deaths = Info_dict["Deaths"]
    Recovered = Info_dict["Recovered"]
    Table_Info = Info_dict["Table_Info"]

    Country = Table_Info[0]
    Total_Cases = Table_Info[1]
    New_Cases = Table_Info[2]
    Total_Deaths = Table_Info[3]
    New_Deaths = Table_Info[4]
    Total_Recoverd = Table_Info[5]
    Active_Cases = Table_Info[6]
    Serious_Critical = Table_Info[7]
    Tot_Cases_1Mpop = Table_Info[8]

    #step3: create plot
    plot_src = Draw_plot.get_plot(Country, Total_Cases)

    return  render_template(
        "index.htm",Coronavirus_Cases=Coronavirus_Cases,Deaths=Deaths,Recovered=Recovered,
        Country=Country,Total_Cases=Total_Cases,New_Cases=New_Cases,Total_Deaths=Total_Deaths,New_Deaths=New_Deaths,
        Total_Recoverd=Total_Recoverd,Active_Cases=Active_Cases,Serious_Critical=Serious_Critical,Tot_Cases_1Mpop=Tot_Cases_1Mpop,
        Plot_Src=plot_src)