'''
Copyright (C) 2021-2022 ETH Zurich and University of Bologna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

'''
Authors: Davide Nadalini
'''

"""
LAYER TEMPLATES
"""

def linear_template_FW(layer_number):
    # template = "  pulp_linear_fp32_fw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, MATMUL_TYPE_FW_L"+str(layer_number)+");\n"
    template = "  pulp_linear_fp32_fw_cl(&l"+str(layer_number)+"_args);\n"
    return template

def linear_template_BW(layer_number):
    # template = "  pulp_linear_fp32_bw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(skip_in_grad)+", MATMUL_TYPE_WG_L"+str(layer_number)+", MATMUL_TYPE_IG_L"+str(layer_number)+");\n"
    template = "  pulp_linear_fp32_bw_cl(&l"+str(layer_number)+"_args);\n"
    return template



def conv2d_template_FW(layer_number):
    # template = "  pulp_conv2d_fp32_fw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(pad)+", "+str(stride_w)+", "+str(stride_h)+", im2col_buffer, MATMUL_TYPE_FW_L"+str(layer_number)+");\n"
    template = "  pulp_conv2d_fp32_fw_cl(&l"+str(layer_number)+"_args);\n"
    return template

def conv2d_template_BW(layer_number):
    # template = "  pulp_conv2d_fp32_bw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(pad)+", "+str(stride_w)+", "+str(stride_h)+", im2col_buffer, bt_buffer, "+str(skip_in_grad)+", MATMUL_TYPE_WG_L"+str(layer_number)+", MATMUL_TYPE_IG_L"+str(layer_number)+");\n"
    template = "  pulp_conv2d_fp32_bw_cl(&l"+str(layer_number)+"_args);\n"
    return template



def DW_template_FW(layer_number):
    # template = "  pulp_conv_dw_fp32_fw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(pad)+", im2col_buffer, MATMUL_TYPE_FW_L"+str(layer_number)+");\n"
    template = "  pulp_conv_dw_fp32_fw_cl(&l"+str(layer_number)+"_args);\n"
    return template

def DW_template_BW(layer_number):
    # template = "  pulp_conv_dw_fp32_bw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(pad)+", im2col_buffer, "+str(skip_in_grad)+", MATMUL_TYPE_WG_L"+str(layer_number)+", MATMUL_TYPE_IG_L"+str(layer_number)+");\n"
    template = "  pulp_conv_dw_fp32_bw_cl(&l"+str(layer_number)+"_args);\n"
    return template



def PW_template_FW(layer_number):
    # template = "  pulp_conv_pw_fp32_fw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(pad)+", MATMUL_TYPE_FW_L"+str(layer_number)+");\n"
    template = "  pulp_conv_pw_fp32_fw_cl(&l"+str(layer_number)+"_args);\n"
    return template

def PW_template_BW(layer_number):
    # template = "  pulp_conv_pw_fp32_bw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(pad)+", "+str(skip_in_grad)+", MATMUL_TYPE_WG_L"+str(layer_number)+", MATMUL_TYPE_IG_L"+str(layer_number)+");\n"
    template = "  pulp_conv_pw_fp32_bw_cl(&l"+str(layer_number)+"_args);\n"
    return template




"""
ACTIVATIONS TEMPLATES
"""

def ReLU_template_FW(layer_number):
    # template = "  pulp_relu_fp32_fw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_out);\n"
    template = "  pulp_relu_fp32_fw_cl(&l"+str(layer_number)+"_args);\n"
    return template

def ReLU_template_BW(layer_number):
    # template = "  pulp_relu_fp32_bw_cl(&layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_out);\n"
    template = "  pulp_relu_fp32_bw_cl(&l"+str(layer_number)+"_args);\n"
    return template


"""
POOLING TEMPLATES
"""

def AvgPool_template_FW(layer_number):
    template = "  pi_cl_team_fork(NUM_CORES, pulp_avgpool_fp32_fw_cl, &l"+str(layer_number)+"_pool_args);\n"
    return template

def AvgPool_template_BW(layer_number):
    template = "  pi_cl_team_fork(NUM_CORES, pulp_avgpool_fp32_bw_cl, &l"+str(layer_number)+"_pool_args);\n"
    return template


def MaxPool_template_FW(layer_number):
    template = "  pi_cl_team_fork(NUM_CORES, pulp_maxpool_fp32_fw_cl, &l"+str(layer_number)+"_pool_args);\n"
    return template

def MaxPool_template_BW(layer_number):
    template = "  pi_cl_team_fork(NUM_CORES, pulp_maxpool_fp32_bw_cl, &l"+str(layer_number)+"_pool_args);\n"
    return template




"""
CONFIGURATION STRUCTURE TEMPLATES
"""

def linear_config_template(layer_number, skip_in_grad):
    template  = "  l"+str(layer_number)+"_args.input = &layer"+str(layer_number)+"_in;\n"
    template += "  l"+str(layer_number)+"_args.coeff = &layer"+str(layer_number)+"_wgt;\n"
    template += "  l"+str(layer_number)+"_args.output = &layer"+str(layer_number)+"_out;\n"
    template += "  l"+str(layer_number)+"_args.skip_in_grad = "+str(skip_in_grad)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_fw = MATMUL_TYPE_FW_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_wg = MATMUL_TYPE_WG_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_ig = MATMUL_TYPE_IG_L"+str(layer_number)+";\n"
    return template

def conv2d_config_template(layer_number, pad_h, pad_w, stride_h, stride_w, skip_in_grad):
    template  = "  l"+str(layer_number)+"_args.input = &layer"+str(layer_number)+"_in;\n"
    template += "  l"+str(layer_number)+"_args.coeff = &layer"+str(layer_number)+"_wgt;\n"
    template += "  l"+str(layer_number)+"_args.output = &layer"+str(layer_number)+"_out;\n"
    template += "  l"+str(layer_number)+"_args.skip_in_grad = "+str(skip_in_grad)+";\n"
    template += "  l"+str(layer_number)+"_args.Lpad = "+str(pad_w)+";\n"
    template += "  l"+str(layer_number)+"_args.Rpad = "+str(pad_w)+";\n"
    template += "  l"+str(layer_number)+"_args.Upad = "+str(pad_h)+";\n"
    template += "  l"+str(layer_number)+"_args.Dpad = "+str(pad_h)+";\n"
    template += "  l"+str(layer_number)+"_args.stride_h = "+str(stride_h)+";\n"
    template += "  l"+str(layer_number)+"_args.stride_w = "+str(stride_w)+";\n"
    template += "  l"+str(layer_number)+"_args.i2c_buffer = im2col_buffer;\n"
    template += "  l"+str(layer_number)+"_args.bt_buffer = bt_buffer;\n"
    template += "  l"+str(layer_number)+"_args.HWC = 0;\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_fw = MATMUL_TYPE_FW_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_wg = MATMUL_TYPE_WG_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_ig = MATMUL_TYPE_IG_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.USE_IM2COL = 1;\n"
    template += "  l"+str(layer_number)+"_args.USE_DMA_IM2COL = 0;\n"
    return template

def DW_config_template(layer_number, pad_h, pad_w, stride_h, stride_w, skip_in_grad):
    template  = "  l"+str(layer_number)+"_args.input = &layer"+str(layer_number)+"_in;\n"
    template += "  l"+str(layer_number)+"_args.coeff = &layer"+str(layer_number)+"_wgt;\n"
    template += "  l"+str(layer_number)+"_args.output = &layer"+str(layer_number)+"_out;\n"
    template += "  l"+str(layer_number)+"_args.skip_in_grad = "+str(skip_in_grad)+";\n"
    template += "  l"+str(layer_number)+"_args.Lpad = "+str(pad_w)+";\n"
    template += "  l"+str(layer_number)+"_args.Rpad = "+str(pad_w)+";\n"
    template += "  l"+str(layer_number)+"_args.Upad = "+str(pad_h)+";\n"
    template += "  l"+str(layer_number)+"_args.Dpad = "+str(pad_h)+";\n"
    template += "  l"+str(layer_number)+"_args.i2c_buffer = im2col_buffer;\n"
    template += "  l"+str(layer_number)+"_args.HWC = 0;\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_fw = MATMUL_TYPE_FW_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_wg = MATMUL_TYPE_WG_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_ig = MATMUL_TYPE_IG_L"+str(layer_number)+";\n"
    return template

def PW_config_template(layer_number, skip_in_grad):
    # &layer"+str(layer_number)+"_in, &layer"+str(layer_number)+"_wgt, &layer"+str(layer_number)+"_out, "+str(pad)+", MATMUL_TYPE_FW_L"+str(layer_number)+"
    template  = "  l"+str(layer_number)+"_args.input = &layer"+str(layer_number)+"_in;\n"
    template += "  l"+str(layer_number)+"_args.coeff = &layer"+str(layer_number)+"_wgt;\n"
    template += "  l"+str(layer_number)+"_args.output = &layer"+str(layer_number)+"_out;\n"
    template += "  l"+str(layer_number)+"_args.skip_in_grad = "+str(skip_in_grad)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_fw = MATMUL_TYPE_FW_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_wg = MATMUL_TYPE_WG_L"+str(layer_number)+";\n"
    template += "  l"+str(layer_number)+"_args.opt_matmul_type_ig = MATMUL_TYPE_IG_L"+str(layer_number)+";\n"
    return template

def ReLU_config_template(layer_number):
    template  = "  l"+str(layer_number)+"_args.input = &layer"+str(layer_number)+"_in;\n"
    template += "  l"+str(layer_number)+"_args.output = &layer"+str(layer_number)+"_out;\n"
    return template

# def MaxPool_config_template(layer_number):
#     template  = "  l"+str(layer_number)+"_args. ;\n"
#     template += "  l"+str(layer_number)+"_args. ;\n"
#     template += "  l"+str(layer_number)+"_args. ;\n"
#     template += "  l"+str(layer_number)+"_args. ;\n"
#     template += "  l"+str(layer_number)+"_args. ;\n"
#     template += "  l"+str(layer_number)+"_args. ;\n"
#     return template

# def AvgPool_config_template(layer_number):
#     template = "  "
#     return template
