import System.IO

isLetter :: Char -> Bool
isLetter c = (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z'))

rmdumps :: [[Char]] -> [Char]
rmdumps [] = "true"
rmdumps (x:xs) | x `elem` xs    = x
               | otherwise = rmdumps xs

-- 同じものがあったらFalse
-- なかったらTrue
main :: IO ()
main = do
    handle <- openFile "../word.txt" ReadMode
    text <- hGetContents handle
    let xs = lines text
    print $ rmdumps $ map (\x -> (takeWhile isLetter x)) xs
    hClose handle
