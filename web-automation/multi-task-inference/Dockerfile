From pytorch/pytorch:2.3.0-cuda11.8-cudnn8-devel
COPY . /flask_demo						
RUN pip install Flask
WORKDIR /flask_demo	
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True
ENV FLASK_APP=flask_demo/app.py
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]