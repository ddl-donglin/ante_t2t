# ante_t2t

Tensorflow1.8 + CUDA9.0 + python3.6 + Tensor2tensor

Run the commands below in terminal:
eg.
# PROBLEM_NAME='attention_gru'
# DATA_DIR='../train_data_atte'
# OUTPUT_DIR='../output_atte'
# t2t-datagen --t2t_usr_dir=. --data_dir=$DATA_DIR --tmp_dir=../tmp_data --problem=$PROBLEM_NAME
# t2t-trainer --t2t_usr_dir=. --data_dir=$DATA_DIR --problem=$PROBLEM_NAME --model=transformer --hparams_set=transformer_base --output_dir=$OUTPUT_DIR
