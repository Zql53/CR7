import streamlit as st
import ollama
# 连接本地的ollama模型
client = ollama.Client(host='http://localhost:11434')
def get_response(messages):
    # 连接模型以及角色，然后开始聊天
    result = client.chat(
        model = 'qwen:0.5b',
        # 最多保留20条消息
        messages = messages[-20:],
        stream=False
    )
    return result.message.content

# 标题
st.title('黑马聊天机器人')
# 分割线
st.divider()
# 判断消息列表是否在会话状态字典中存在，如果不存在则创建
if 'messages' not in st.session_state:
    st.session_state.messages = [{'role':'assistant','content':'你好,我是黑马聊天机器人,我可以回答你的问题'}]
# 构建聊天窗口
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])
# 用户输入问题
promt = st.chat_input('请输入你的问题')
if promt:
    st.chat_message('user').write(promt)
    st.session_state.messages.append({'role':'user','content':promt})
    with st.spinner('思考中...'):
        # 调用模型获取响应
        response = get_response(st.session_state.messages)
        st.chat_message('assistant').write(response)
        st.session_state.messages.append({'role':'assistant','content':response})




















