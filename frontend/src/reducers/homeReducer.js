const initialState = {
    loading: true,
    count: 0,
};
const homeReducer = (state = initialState, action) => {
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
export default homeReducer