const initialState = {
    isLogin: false,
};
const loginReducer = (state = initialState, action) => {
    switch (action.type) {
        case "increase":
            return {
                ...state,
                ...action.payload
            };
        default:
            return state;
    }
}
export default loginReducer