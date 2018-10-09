in_dir=../../MII_LIEPA_SYN_V1/Regina/data
out_dir=./
in_1_id=5052
in_2_id=5086

pause=0.0
ffmpeg -y -i $in_dir/$in_1_id.wav -i $in_dir/$in_2_id.wav -filter_complex "aevalsrc=exprs=0:d=$pause[silence], [0:a] [silence] [1:a] concat=n=3:v=0:a=1[outa]" -map [outa] $out_dir/$in_1_id-$in_2_id.mp3