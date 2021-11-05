import { INCREMENT, DECREMENT } from "../reducers/counterReducer";

export function increment() {
  return {
    type: INCREMENT,
  };
}

export function decrement() {
  return {
    type: DECREMENT,
  };
}
