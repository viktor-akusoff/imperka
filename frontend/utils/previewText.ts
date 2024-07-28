export default function (text: String, maxLength: number = 256) {
    if (text.length <= maxLength) {
        return text;
    }

    const truncatedText = text.substring(0, maxLength);
    const lastSpaceIndex = truncatedText.lastIndexOf(' ');
    
    return lastSpaceIndex !== -1 
        ? `${truncatedText.substring(0, lastSpaceIndex)}...`
        : `${truncatedText}...`; 
}