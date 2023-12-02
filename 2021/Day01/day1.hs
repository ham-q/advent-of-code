import System.IO

main :: IO ()
main = do
   myFile <- readFile (openFile "hello.txt" ReadMode)
   hClose myFile
   putStrLn "done!"