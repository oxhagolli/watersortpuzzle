/**
 * Drawing functionality
 */

function setup() {
  createCanvas(900, 400);
}

const drawVial = (n) => {
  fill(255);
  for (let i = 0; i < n; i++) {
    rect(50 + i * 52, 50, 50, 200, 0, 0, 20, 20);
  }
};

const drawCol = (n, pos, color) => {
  // n is the 0-based index of vial
  // pos is the 0-based pos of the color from top to bottom
  const x = 50 + n * 52;
  const y = 50 + pos * 50;
  const corner = pos == 3 ? 20 : 0;
  fill(color);
  rect(x, y, 50, 50, 0, 0, corner, corner);
};

const colorMap = {
  1: "#FF930F",
  2: "#63FF0F",
  3: "#0FFFF7",
  4: "#1C0FFF",
  5: "#FF0FF5",
  6: "#188126",
  7: "#551881",
  8: "#F8E612",
  9: "#F0001A",
  10: "#45A3E8",
  11: "#9C3F26",
  12: "#A6A6A6",
};

const drawState = (state) => {
  // state = matrix [[color1, color2, color3, color4], [...]]
  state.forEach((vial, i) => {
    vial.forEach((color, j) => {
      drawCol(i, j + (4 - vial.length), colorMap[color]);
    });
  });
};

let state = [
  [1, 2, 3, 4],
  [5, 6, 1, 7],
  [8, 4, 6, 9],
  [9, 5, 7, 9],
  [10, 2, 9, 1],
  [3, 11, 8, 12],
  [4, 12, 11, 5],
  [1, 6, 4, 5],
  [11, 3, 11, 12],
  [6, 8, 7, 10],
  [12, 2, 7, 10],
  [2, 8, 10, 3],
  [],
  [],
];

function draw() {
  background(255);
  drawVial(14);
  drawState(state);
}

/**
 * Puzzle solving
 */

const is_solved = (current) => {
  return (
    current.filter((vial) => {
      return new Set(vial).size > 1;
    }).size == 0
  );
};

const deepcopy = (current) => {
  return current.map((vial) => [...vial]);
};

const move = (current, a, b, timeout = 0) => {
  if (current[a].length == 0 || current == undefined) {
    return;
  }
  current = deepcopy(current);
  // get depth at a
  const left = current[a];
  let i = 0;
  const top = left[i];
  let depth = [];
  while (left[i] == top) {
    depth.push(left[i]);
    i++;
  }

  // prepend to b loc
  const right = current[b];
  if (
    depth.length > 4 - right.length ||
    (right.length != 0 && depth[0] != right[0])
  ) {
    return;
  }
  current[b] = depth.concat(right);
  current[a] = left.splice(depth.length);
  setTimeout(function () {}, timeout);
  return current;
};

const backtrack = (current, previous = []) => {
  state = move(state, 0, 12);
  state = move(state, 0, 13);
  state = move(state, 11, 13);
};

backtrack(state);
