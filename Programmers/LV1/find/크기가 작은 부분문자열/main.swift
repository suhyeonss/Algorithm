//
//  main.swift
//  find
//
//  Created by suhyeonss on 6/26/24.
//
import Foundation

func solution(_ t: String, _ p: String) -> Int {
    var cnt = 0
    for i in 0 ... (t.count - p.count) {
        let start = t.index(t.startIndex, offsetBy: i)
        let end = t.index(t.startIndex, offsetBy: i + p.count)
        if t[start ..< end] <= p {
            cnt += 1
        }
    }
    return cnt
}

// print("solution = \(solution("3141592", "271"))")
// print("solution = \(solution("500220839878", "7"))")
// print("solution = \(solution("10203", "15"))")
