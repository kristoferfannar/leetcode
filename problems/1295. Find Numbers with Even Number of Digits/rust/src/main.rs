struct Solution;

impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        let mut count = 0;
        for mut ele in nums {
            let mut digits = 0;
            while ele > 0 {
                digits += 1;
                ele /= 10;
            }

            if digits % 2 == 0 {
                count += 1;
            }
        }
        return count;
    }
}
fn main() {
    assert!(Solution::find_numbers([12,345,2,6,7896].to_vec()) == 2);
}
