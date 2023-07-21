import sys
from flask import Flask,request,render_template,jsonify
from src.exception import CustomException
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

from src.pipeline.train_pipeline import TrainPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()

        return jsonify("Training Successfull.")

    except Exception as e:
        raise CustomException(e,sys)

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('index.html')
    
    else:
        data = CustomData(
        cement=float(request.form['cement']),
        blastFurnace=float(request.form['blastFurnace']),
        flyAsh=float(request.form['flyAsh']),
        water=float(request.form['water']),
        superplasticizer=float(request.form['superplasticizer']),
        courseAggregate=float(request.form['courseAggregate']),
        fineaggregate=float(request.form['fineaggregate']),
        age=int(request.form['age'])
    )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)
        print(results)

        return render_template('index.html',final_result='Cement Strength is : {} '.format(results))
    

if __name__=="__main__":
    app.run()