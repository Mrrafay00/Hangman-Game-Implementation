import random

def hangman():
    # Predefined list of words
    word_list = [
    'abandon', 'ability', 'abroad', 'absolute', 'academy', 'account', 'accurate', 'achieve', 'acquire', 'activity',
    'addition', 'address', 'advance', 'adventure', 'advice', 'affect', 'africa', 'agency', 'agreement', 'aircraft',
    'airport', 'alcohol', 'algebra', 'alliance', 'alphabet', 'america', 'ancient', 'animal', 'announce', 'answer',
    'antarctica', 'antenna', 'anxiety', 'apology', 'apparatus', 'appeal', 'apple', 'application', 'approach', 'approval',
    'arabia', 'architecture', 'argument', 'arithmetic', 'army', 'arrival', 'article', 'artist', 'asia', 'assembly',
    'astronomy', 'athlete', 'atmosphere', 'atom', 'attack', 'attempt', 'attention', 'attitude', 'audience', 'australia',
    'authority', 'automatic', 'autumn', 'average', 'aviation', 'balance', 'balloon', 'banana', 'banking', 'battery',
    'beautiful', 'because', 'bedroom', 'behavior', 'belief', 'benefit', 'biology', 'birthday', 'blanket', 'border',
    'bottle', 'brain', 'branch', 'bread', 'bridge', 'brother', 'building', 'business', 'butter', 'calendar',
    'camera', 'campaign', 'canada', 'capital', 'captain', 'carbon', 'career', 'carpet', 'cartoon', 'castle',
    'category', 'celebrate', 'century', 'ceremony', 'challenge', 'champion', 'chapter', 'character', 'charity', 'chemical',
    'chemistry', 'children', 'choice', 'church', 'citizen', 'civilization', 'climate', 'clock', 'clothing', 'college',
    'comfort', 'command', 'commerce', 'committee', 'communication', 'community', 'company', 'competition', 'computer', 'concept',
    'conclusion', 'condition', 'conference', 'confidence', 'conflict', 'connection', 'conservation', 'constitution', 'construction', 'continent',
    'contract', 'control', 'conversation', 'cooperation', 'country', 'courage', 'creation', 'creativity', 'criminal', 'culture',
    'currency', 'customer', 'database', 'daughter', 'decision', 'definition', 'democracy', 'department', 'development', 'diamond',
    'dictionary', 'difference', 'difficulty', 'direction', 'discovery', 'discussion', 'disease', 'distance', 'distribution', 'division',
    'doctor', 'document', 'education', 'effect', 'efficiency', 'electricity', 'element', 'elephant', 'emotion', 'empire',
    'employee', 'energy', 'engine', 'engineering', 'english', 'environment', 'equipment', 'europe', 'evidence', 'example',
    'exchange', 'exercise', 'experiment', 'explanation', 'exploration', 'factory', 'family', 'farmer', 'fashion', 'feature',
    'festival', 'finance', 'finger', 'fire', 'fish', 'flight', 'flower', 'football', 'forest', 'formula',
    'foundation', 'freedom', 'friend', 'future', 'galaxy', 'garden', 'geography', 'geology', 'government', 'grammar',
    'gravity', 'growth', 'happiness', 'harbor', 'hardware', 'health', 'history', 'holiday', 'hospital', 'human',
    'hurricane', 'hydrogen', 'identity', 'imagination', 'importance', 'improvement', 'industry', 'information', 'innovation', 'insect',
    'inspiration', 'instruction', 'insurance', 'intelligence', 'interest', 'internet', 'interview', 'investment', 'island', 'journal',
    'journey', 'justice', 'keyboard', 'kingdom', 'knowledge', 'language', 'library', 'light', 'literature', 'machine',
    'magazine', 'manager', 'market', 'mathematics', 'medicine', 'memory', 'message', 'method', 'microscope', 'military',
    'mineral', 'minute', 'mission', 'mobile', 'modern', 'mountain', 'movement', 'museum', 'music', 'nation',
    'natural', 'navigation', 'network', 'newspaper', 'nutrition', 'object', 'observation', 'ocean', 'office', 'operation',
    'opinion', 'opportunity', 'organization', 'oxygen', 'painting', 'paragraph', 'parent', 'parliament', 'particle', 'partnership',
    'passport', 'patient', 'pattern', 'peace', 'percentage', 'performance', 'period', 'permission', 'personality', 'philosophy',
    'photograph', 'physics', 'planet', 'plastic', 'platform', 'poetry', 'police', 'politics', 'pollution', 'population',
    'position', 'possibility', 'practice', 'prediction', 'preparation', 'president', 'pressure', 'prevention', 'principle', 'prison',
    'problem', 'process', 'production', 'profession', 'program', 'programming', 'project', 'property', 'protection', 'protein',
    'psychology', 'publication', 'quality', 'quantity', 'question', 'railway', 'reaction', 'reading', 'reality', 'reason',
    'recognition', 'recommendation', 'record', 'recycling', 'reflection', 'region', 'relationship', 'religion', 'remember', 'research',
    'resource', 'respect', 'responsibility', 'restaurant', 'revolution', 'river', 'rocket', 'science', 'scientist', 'security',
    'sentence', 'service', 'software', 'solution', 'source', 'space', 'speaker', 'species', 'speech', 'sport',
    'standard', 'statement', 'station', 'strategy', 'strength', 'student', 'subject', 'success', 'suggestion', 'summer',
    'support', 'surface', 'surprise', 'survey', 'system', 'teacher', 'technology', 'telephone', 'television', 'temperature',
    'territory', 'theory', 'thought', 'thunder', 'tourism', 'tradition', 'transport', 'travel', 'treasure', 'treatment',
    'universe', 'university', 'vacation', 'valuable', 'variable', 'victory', 'village', 'violence', 'vision', 'volcano',
    'volume', 'volunteer', 'warning', 'weather', 'website', 'welcome', 'wilderness', 'window', 'wisdom', 'worker',
    'writing', 'yesterday', 'youth', 'zoology'
]
    
    # Choose a random word
    secret_word = random.choice(word_list).lower()
    word_length = len(secret_word)
    
    # Game state variables
    display_word = ['_'] * word_length
    guessed_letters = []
    attempts_left = 15
    game_over = False
    
    print("=" * 50)
    print("Welcome to Hangman!")
    print("=" * 50)
    print(f"The word has {word_length} letters.")
    print("You have 15 attempts to guess the word.")
    print("-" * 50)
    
    while not game_over:
        # Display current state
        print(f"\nWord: {' '.join(display_word)}")
        print(f"Attempts remaining: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get player's guess
        guess = input("\nGuess a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter (A-Z).")
            continue
        
        if guess in guessed_letters:
            print(f"️ You already guessed '{guess}'. Try a different letter.")
            continue
        
        # Add to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update display word
            for i in range(word_length):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print(f" Sorry, '{guess}' is not in the word.")
            attempts_left -= 1
        
        # Check win condition
        if '_' not in display_word:
            print("\n" + "=" * 50)
            print(f" CONGRATULATIONS! You guessed the word: {secret_word}")
            print(f" You won with {attempts_left} attempts remaining!")
            print("=" * 50)
            game_over = True
            break
        
        # Check lose condition
        if attempts_left == 0:
            print("\n" + "=" * 50)
            print(f" GAME OVER! You've run out of attempts.")
            print(f" The word was: {secret_word}")
            print("=" * 50)
            game_over = True
            break
        
        # Display a separator for better readability
        print("-" * 50)
    
    # Ask if player wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again.startswith('y'):
        hangman()  # Restart the game
    else:
        print("\nThanks for playing! Goodbye!")

# Start the game
if __name__ == "__main__":
    hangman()
