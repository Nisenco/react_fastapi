const initialState = {
    isLogin: false,
};
const loginReducer = (state = initialState, action) => {
    switch (action.type) {
        case "SET_LOGIN":
            return {
                ...state,
                ...action.payload
            };
        default:
            return state;
    }
}
export default loginReducer