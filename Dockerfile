FROM python:alpine

# Include in our base image the packages we know we *absolutely* need for a HoW
RUN pip install --no-cache-dir sphinx \
		sphinx-autobuild \
		sphinxcontrib-fulltoc==1.2.0 \
		sphinx-bootstrap-theme==0.6.0 \
		sphinx_fontawesome

# Declare 2 volumes:
# - /src -> Source folder containing ReStructured Text files
# - /out -> Output folder that will contain the built HTML files
# NOTE: We explicitely don't define a VOLUME directive here to be able to check
# from the running container if those 2 volumes are mountpoints or not. If we
# did declare a VOLUME for those here, they would always be mountpoints.

# Expose container port 8000/tcp (for the live build)
EXPOSE 8000

COPY docker-entrypoint.py /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.py"]
CMD ["-h"]
