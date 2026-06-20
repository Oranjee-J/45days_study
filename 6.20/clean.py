import os
from langchain_community.document_loaders import PyMuPDFLoader


def clean_pdf(file_path):
    """
    清洗 PDF 并保存为 txt 文件

    Parameters
    ----------
    file_path : str
        PDF 文件路径

    save_dir : str
        清洗后文件保存目录

    Returns
    -------
    str
        清洗后 txt 文件路径
    """

    loader = PyMuPDFLoader(file_path)
    docs = loader.load()

    print(f"原始页数：{len(docs)}")

    cleaned_text = ""

    remove_patterns = [
        "Attention Is All You Need",
        "31st Conference on Neural Information Processing Systems (NIPS 2017)"
    ]

    for doc in docs:

        text = doc.page_content

        if "References" in text:
            text = text.split("References")[0]
            cleaned_text += text
            break

        text = text.replace("\n", " ")
        text = " ".join(text.split())

        for pattern in remove_patterns:
            text = text.replace(pattern, "")

        cleaned_text += text + "\n\n"



    file_name = os.path.basename(file_path)
    file_name = os.path.splitext(file_name)[0]

    save_path = f"{file_name}_clean.txt"

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"清洗后的文档已保存：{save_path}")

    return save_path


clean_file = clean_pdf("paper.pdf")