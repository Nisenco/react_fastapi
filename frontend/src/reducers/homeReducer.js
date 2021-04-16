const initialState = {
    dataSource: [],
    loading: true,
    id: '',
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