import torch

from utils.dump_utils import tensor_to_string
from utils.torch_to_trainlib import VIT_COMPONENTS_WRITERS

IMPLEMENTED_DATA_TYPES = ["fp32"]


def header_writer(data_type):
    # Open file
    f = open("net_args.h", "w")

    # Introductory elements
    if data_type == "fp32":
        f.write("// FLOAT 32 ViT model\n")
        f.write("#define FLOAT32\n\n")

    # Write necessary dimensions

    # Close file
    f.close()

    return None


def input_writer(data, data_type):
    # Check passed arguments
    assert isinstance(data, torch.Tensor), "Invalid data"

    # Open file
    f = open("input_sequence.h", "w")

    # Introductory elements
    if data_type == "fp32":
        data_marker = "float"
    else:
        data_marker = None
    f.write("#define INPUT_SIZE " + str(data.numel()) + "\n\n")

    # Write actual data
    f.write(
        "PI_L2 "
        + data_marker
        + " INPUT[INPUT_SIZE] = {"
        + tensor_to_string(data)
        + "};\n\n"
    )

    # Close file
    f.close()

    return None


def model_writer(model, data_type):
    # Check passed arguments
    assert isinstance(model, torch.nn.Module), "Invalid model"

    # Open file
    f = open("model_defines.h", "w")

    # Introductory elements
    if data_type == "fp32":
        data_marker = "float"
    else:
        data_marker = None

    # Write actual data
    for i, (name, el) in enumerate(model.named_parameters()):
        print("[" + str(i) + "] Working on: " + name)
        if "patch_embedding" not in name:
            continue

        f.write(
            "PI_L2 "
            + data_marker
            + " "
            + name.replace(".", "_").upper()
            + "["
            + str(el.numel())
            + "] = {"
            + tensor_to_string(el)
            + "};\n\n"
        )

    # Close file
    f.close()

    return None


def output_writer(data, data_type):
    # Check passed arguments
    assert isinstance(data, torch.Tensor), "Invalid data"

    # Open file
    f = open("output_sequence.h", "w")

    # Introductory elements
    if data_type == "fp32":
        data_marker = "float"
    else:
        data_marker = None
    f.write("#define OUTPUT_SIZE " + str(data.numel()) + "\n\n")

    # Write actual data
    f.write(
        "PI_L2 "
        + data_marker
        + " OUTPUT[OUTPUT_SIZE] = {"
        + tensor_to_string(data)
        + "};\n\n"
    )

    # Close file
    f.close()

    return None


def model_components_writer(ordered_nodes, all_nodes, data_type):
    # Introductory elements
    if data_type == "fp32":
        data_marker = "float"
    else:
        data_marker = None

    structures_and_blobs = ""
    blob_initializations = ""
    blob_connect = ""

    # Write actual data
    for node in ordered_nodes:
        if node in VIT_COMPONENTS_WRITERS.keys():
            all_nodes[node]["input_shape"] = all_nodes[all_nodes[node]["input_from"]][
                "output_shape"
            ]

            text_content = VIT_COMPONENTS_WRITERS[node](
                component_name=node,
                component=all_nodes[node],
                data_marker=data_marker,
            )

            if text_content is not None:
                structures_and_blobs += text_content[0]
                blob_initializations += text_content[1]
                blob_connect += text_content[2]

    # Write to header
    f = open("model_components.h", "w")

    f.write("// =============== Includes ===============\n")
    f.write("#include \"input_sequence.h\"\n")
    f.write("#include \"model_defines.h\"\n")
    f.write("\n")

    f.write("// =============== Constants definition ===============\n")
    f.write("PI_L1 float zero_init = 0.0f;\n")
    f.write("PI_L1 float min_float = -340282346638528859811704183484516925440.0f;\n")
    f.write("\n")

    f.write("// =============== Structures and blobs definition ===============\n")
    f.write(structures_and_blobs)

    f.write("void init_and_connect_blobs();\n")

    f.close()

    # Write to file
    f = open("model_components.c", "w")

    f.write("#include \"model_components.h\"\n")
    f.write("\n")

    f.write("void init_and_connect_blobs() {\n")
    f.write("\t")
    f.write("// =============== Initializations ===============\n")
    f.write(blob_initializations)

    f.write("\t")
    f.write(
        "// =============== Populating and connecting blobs to structures ===============\n"
    )
    f.write(blob_connect)

    f.write("}\n")
    f.close()

    return None
