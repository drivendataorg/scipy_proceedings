dot -Tpng -Gdpi=300 videos.dot -o fig-video-pipeline-flow.png
dot -Tsvg videos.dot -o fig-video-pipeline-flow.svg

dot -Tpng -Gdpi=300 images.dot -o fig-image-pipeline-flow.png
dot -Tsvg images.dot -o fig-image-pipeline-flow.svg


dot -Tpng -Gdpi=300 depth.dot -o fig-depth-pipeline-flow.png
dot -Tsvg depth.dot -o fig-depth-pipeline-flow.svg
