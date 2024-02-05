FROM pywaterflood:latest
COPY --chown=pywaterflood:pywaterflood ./run_crm.py /home/pywaterflood/
WORKDIR /home/pywaterflood
RUN mkdir /home/pywaterflood/results && chown pywaterflood:pywaterflood /home/pywaterflood/results
ENTRYPOINT [ "python", "/home/pywaterflood/run_crm.py" ]