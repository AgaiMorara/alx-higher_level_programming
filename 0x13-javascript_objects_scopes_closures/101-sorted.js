#!/usr/bin/node
// 101-sorted - imports a dicrionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const {dict} = require('./101-data').dict;

const result = {};

Object.entries(dict).forEach(([userId, occurrence]) => {
  if (!result[occurrence]) {
    result[occurrence] = [];
  }
  result[occurrence].push(userId);
});
